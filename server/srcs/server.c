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
	printf("the big fd is : %d\n", big_fd);
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
	int	tmp;
	struct	sockaddr_in	s_sin_client;
	socklen_t	s_sin_size = sizeof(s_sin_client);
	
	if (FD_ISSET(server->fd, &readfds)){
		tmp = accept(server->fd, (struct sockaddr *)&s_sin_client, &s_sin_size);
		if (tmp == -1)
			perror("accept :");
		server->fds[server->nb_fd] = tmp;
		server->nb_fd++;
		server->fds = realloc(server->fds, sizeof(int) * (server->nb_fd + 1));
		printf("add a new connect %d\n", server->nb_fd);
		return (0);
	}
	for (int i = 0; i < server->nb_fd; i++){
		if (FD_ISSET(server->fds[i], &readfds)){
			int	check = i;
			char	*str = getnextline(server->fds[i]);
			if (str == NULL)
				return (0);
			for (int j = 0; j < server->nb_fd; j++){
				if (j == check)
					j++;
				dprintf(server->fds[j], "he say: %s", str);
			}
		}
	}
	return (0);
}

int	check_fd(t_parse *parse, server_t *server, fd_set readfds)
{
	int	best_fd = big_fd(server);
		
	FD_ZERO(&readfds);
	FD_SET(server->fd, &readfds);
	for (int i = 0; i < server->nb_fd; i++){
		printf("set fd\n");
		FD_SET(server->fds[i], &readfds);
	}
	printf("%d\n", best_fd);
	printf("%d\n", server->fd);
	if (select((server->fd > best_fd ? server->fd : best_fd) + 1, &readfds,
		NULL, NULL, NULL) != -1){
		if (good_select(readfds, server) == 84)
			return (84);
	}
	else
		perror("select: ");
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