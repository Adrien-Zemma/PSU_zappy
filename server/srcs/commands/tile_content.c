/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	tile_content(server_t *server, client_t *client, char *str)
{
	int	x;
	int	y;

	if (!parse_command(str, ' ', 1) && !parse_command(str, ' ', 2))
		return BAD_PARAM;
	x = atoi(parse_command(str, ' ', 1));
	y = atoi(parse_command(str, ' ', 2));
	if (x >= server->parse->width || y >= server->parse->height)
		return KO;
	draw_tile(server->map, client->fd, x, y);
	return OK;
}