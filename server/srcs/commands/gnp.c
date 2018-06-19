/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	get_number_player(server_t *server, client_t *client, char *str)
{
	int i;

	(void)str;
	dprintf(client->fd, "%d\n", server->nb_client);
	return OK;
}