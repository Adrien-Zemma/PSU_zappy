/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	names_team(server_t *server, client_t *client, char *str)
{
	(void)str;
	dprintf(client->fd, "msz %d %d\n", server->parse->width, server->parse->height);
}