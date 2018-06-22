/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	get_number_player(server_t *server, client_t *client, char *str)
{
	int	nb = 0;

	(void)str;
	for (int i = 0; server->clients[i]; i++)
		nb += (server->clients[i]->id == -1 ? 0 : 1);
	dprintf(client->fd, "gnp %d\n", nb);
	return OK;
}
