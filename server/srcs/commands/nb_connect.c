/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	nb_connect(server_t *server, client_t *client, char *str)
{
	int	nb = 0;

	str = str;
	for (int i = 0; server->clients[i] != NULL; i++) {
		if (strcmp(client->team, server->clients[i]->team) == 0)
			nb++;
	}
	dprintf(client->fd, "%d\n", server->parse->clientsNb - nb);
	return OK;
}
