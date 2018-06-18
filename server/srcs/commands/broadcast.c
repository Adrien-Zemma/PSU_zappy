/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

static void broadcast_client(tile_t ***map, client_t original, client_t target, char *msg)
{
	dprintf(target->fd, "message %d, %s\n", 0, msg);
}

int	broadcast(server_t *server, client_t *client, char *str)
{
	while (*str && *str != ' ')
		str++;
	if (*str == ' ')
		str++;
	else
		return BAD_PARAM;
	for (int i = 0; server->clients[i]; i++)
		if (server->clients[i] != client)
			broadcast_client(server->map, client, server->clients[i], str);
	return OK;
}

