/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	nb_connect(server_t *server, client_t *client, char *str)
{
	(void) server;
	str = str;
	if (!client->team) {
		dprintf(client->fd, "0\n");
		return (KO);
	}
	dprintf(client->fd, "%d\n",
		client->team->max_players - client->team->current_players);
	return (OK);
}
