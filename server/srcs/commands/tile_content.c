/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	tile_content(server_t *server, client_t *client, char *str)
{
	int	x = atoi(parse_command(str, ' ', 1));
	int	y = atoi(parse_command(str, ' ', 2));

	if (x >= server->parse->width || y >= server->parse->height)
		return;
	draw_tile(server->map, client->fd, x, y);
}