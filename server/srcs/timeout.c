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
		if (server->clients[i]->command) {
			time_client = server->clients[i]->command->time;
			break;
		}
	if (!server->clients[i])
		return (NULL);
	for (; server->clients[i] != NULL; i++){
		if (server->clients[i]->command
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

void	remove_time_clients(server_t *server, struct timeval *tv)
{
	if (!tv)
		return;
	for (size_t i = 0; server->clients[i]; i++)
		if (server->clients[i]->command) {
			server->clients[i]->command->time -= tv->tv_sec;
			if (server->clients[i]->command->time <= 0
			|| server->clients[i]->command->time <= 0) {
				server->clients[i]->command->ptrFnct(server,
					server->clients[i],
					server->clients[i]->command->name);
				server->clients[i]->command = NULL;
			}
		}
	return;
}
