/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	eject(server_t *server, client_t *client, char *str)
{
	int clients;
	client_t *tmp;

	(void)str;
	for (clients = 0; server->map[client->pos_y][client->pos_x]->clients[clients]; clients++);
	if (clients == 1) {
		dprintf(client->fd, "ko\n");
		return (KO);
	}
	for (int i = 0; i < clients;) {
		if (server->map[client->pos_y][client->pos_x]->clients[i] != client) {
			tmp = server->map[client->pos_y][client->pos_x]->clients[i];
			push_client(server, tmp, client->orientation);
			clients--;
		}
		else
			i++;
	}
	dprintf(client->fd, "ok\n");
	return (OK);
}
