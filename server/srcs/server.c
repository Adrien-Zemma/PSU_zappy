/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	check_big_fd(server_t *server)
{
	int	big_fd = server->fds[0];
	for (int i = 0; i < server->nb_fd; i++){
		if (server->fds[i] > big_fd)
			big_fd = server->fds[i];
	}
	return (big_fd);
}

int	big_fd(server_t *server)
{
	if (server->nb_fd != 0)
		return (check_big_fd(server));
	else
		return (0);
	return (0);
}

int	good_select(fd_set readfds, server_t *server)
{
	int	ret = 0;

	if (FD_ISSET(server->fd, &readfds))
		return (set_accept(server));
	for (int i = 0; i < server->nb_fd; i++){
		if (FD_ISSET(server->fds[i], &readfds)){
			read_command(server->fds[i], server);
			ret = 1;
		}
	}
	return (ret);
}

int	check_fd(t_parse *parse, server_t *server, fd_set readfds)
{
	int		best_fd = big_fd(server);
	struct timeval	*tv = get_select_timeout(server);
	double		backup_time = tv ? (tv->tv_sec + (double)(tv->tv_usec / 1000000.0f)) : 0;
	int		ret;

	parse = parse;
	FD_ZERO(&readfds);
	FD_SET(server->fd, &readfds);
	for (int i = 0; i < server->nb_fd; i++)
		FD_SET(server->fds[i], &readfds);
	ret = select((server->fd > best_fd ? server->fd : best_fd) + 1, &readfds, NULL, NULL, tv);
	if (ret == -1)
		return (84);
	if (ret != 0)
		backup_time = tv ? (tv->tv_sec + (double)(tv->tv_usec / 1000000.0f)) : 0;
	remove_time_clients(server, backup_time);
	if (good_select(readfds, server) == 84)
		return (84);
	return (0);
}

int	start_server(t_parse *parse, server_t *server)
{
	fd_set	readfds;

	while (42) {
		if (check_fd(parse, server, readfds) == 84)
			return (84);
	}
	return (0);
}
