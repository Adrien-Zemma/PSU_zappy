/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	names_team(server_t *server, client_t *client, char *str)
{
	str = str;
	for (int i = 0; server->parse->teams[i] != NULL; i++)
		dprintf(client->fd, "tna %s\n", server->parse->teams[i]);
	return OK;
}