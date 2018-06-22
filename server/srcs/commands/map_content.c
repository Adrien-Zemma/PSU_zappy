/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	draw_tile(tile_t ***map, int fd, int i, int j)
{
	dprintf(fd, "bct %d %d %d %d %d %d %d %d %d\n",
		j, i, map[i][j]->food, map[i][j]->linemate, map[i][j]->deraumere,
		map[i][j]->sibur, map[i][j]->mendiane,
		map[i][j]->phiras, map[i][j]->thystam);
}

int	map_content(server_t *server, client_t *client, char *str)
{
	(void)str;
	for (int i = 0; server->map[i]; i++)
		for (int j = 0; server->map[i][j]; j++)
			draw_tile(server->map, client->fd, i, j);
	return (OK);
}
