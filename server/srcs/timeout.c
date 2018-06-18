/*
** EPITECH PROJECT, 2018
** zappy
** File description:
** timeout func
*/

#include "server.h"

struct timeval	*get_select_timeout(server_t *server)
{
	struct timeval	*ret = NULL;
	double		time_client = -1;
	size_t		i = 0;

	for (i = 0; server->clients[i]; i++)
		if (server->clients[i]->command && server->clients[i]->command->time > 0) {
			time_client = server->clients[i]->command->time;
			break;
		}
	if (time_client == -1)
		return (NULL);
	for (; server->clients[i] != NULL; i++){
		if (server->clients[i]->command
			&& server->clients[i]->command->time > 0
			&& time_client > server->clients[i]->command->time)
			time_client = server->clients[i]->command->time;
	}
	ret = malloc(sizeof(struct timeval));
	if (!ret)
		return (NULL);
	ret->tv_sec = time_client;
	ret->tv_usec = 0;
	return (ret);
}

void	remove_time_clients(server_t *server, double last_time)
{
	int	state;
	int	check = 0;

	if (last_time <= 0)
		return;
	for (size_t i = 0; server->clients[i]; i++)
		if (server->clients[i]->command) {
			server->clients[i]->command->time -= last_time;
			if (server->clients[i]->command->time <= 0) {
				printf("Client[%d]: Starting %s\n", server->clients[i]->fd, server->clients[i]->command->name);
				state = server->clients[i]->command->ptrFnct(server,
					server->clients[i],
					server->clients[i]->command->name);
				manage_error(server->clients[i]->fd, state, &check);
				server->clients[i]->command = NULL;
				if (!check)
					dprintf(server->clients[i]->fd, "suc:%d\n", check);
			}
		}
	return;
}

command_t	*copy_cmd(command_t *command, char *name)
{
	command_t	*ret = malloc(sizeof(command_t));

	if (!ret)
		return (NULL);
	ret->time = command->time;
	ret->ptrFnct = command->ptrFnct;
	ret->name = name;
	return (ret);
}
