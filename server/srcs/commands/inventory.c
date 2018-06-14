/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	inventory(server_t *server, client_t *client, char *str)
{
	str = str;
	server = server;
	dprintf(client->fd, "[food %d, linemate %d, demaumere %d, sibur %d, mendiane %d, phiras %d, thystame %d]\n",
		client->food, client->linemate, client->demaumere,
		client->sibur, client->mendiane, client->phiras,
		client->thystame);
	return OK;
}