/*
** EPITECH PROJECT, 2018
** zappy
** File description:
** check dead funcs
*/

#include "server.h"

int	dead(server_t *server, client_t *client, char *str)
{
	(void) str;
	dprintf(client->fd, "dead\n");
	for (int i = 0; server->clients[i]; i++)
		if (server->clients[i]->id == -1)
			dprintf(server->clients[i]->fd, "pdi %d\n", client->id);
	remove_client(server, client->fd);
	return (OK);
}

int	check_dead(server_t *server, double t)
{
	const double	food_time = 126.0f / (double)server->parse->freq;

	for (size_t i = 0; server->clients[i]; i++) {
		if (server->clients[i]->id != -1) {
			server->clients[i]->time += t;
			while (server->clients[i]->time - food_time > 0) {
				server->clients[i]->time -= food_time;
				server->clients[i]->food--;
			}
			if (server->clients[i]->food <= 0)
				dead(server, server->clients[i--], NULL);
		}
	}
	return (OK);
}
