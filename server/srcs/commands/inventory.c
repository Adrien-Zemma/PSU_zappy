/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	inventory(server_t *server, client_t *client, char *str)
{
	char	*end = NULL;

	str = str;
	server = server;
	asprintf(&end, ", mendiane %d, phiras %d, thystame %d]\n",
		client->mendiane,
		client->phiras,
		client->thystame);
	dprintf(client->fd, "[food %d, linemate %d, deraumere %d, sibur %d%s",
		client->food,
		client->linemate,
		client->demaumere,
		client->sibur,
		end);
	return (OK);
}
