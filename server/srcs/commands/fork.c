/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	forke(server_t *server, client_t *client, char *str)
{
	str = str;
	for (int i = 0; server->clients[i] != NULL; i++) {
		if (server->clients[i]->id == -1)
			dprintf(server->clients[i]->fd, "pfk %d\n", client->id);
	}
	dprintf(client->fd, "ok\n");
	return (0);
}
