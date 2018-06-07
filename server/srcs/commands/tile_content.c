/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	tile_content(server_t *server, client_t *client, char *str)
{
	(void)str;
	for (int i = 0; server->map[i]; i++) {
		for (int j = 0; server->map[i][j]; j++) {
			dprintf(client->fd, "bct %d %d %d %d %d %d %d %d %d\n",
			i, j, 0, server->map[i][j]->linemate, server->map[i][j]->deraumere,
			server->map[i][j]->sibur, server->map[i][j]->mendiane,
			server->map[i][j]->phiras, server->map[i][j]->thystam);
		}
	}
}