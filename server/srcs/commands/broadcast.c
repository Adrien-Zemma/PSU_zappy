/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"
#include <math.h>

static int smallest_path(int original, int target, int size)
{
	int direct = target - original;
	int indirect = size - ((original > target) ? original : target);
	indirect += ((original > target) ? target : original);
	indirect *= ((original > target) ? 1 : -1);
	return ((fabs(direct) <= fabs(indirect) ? direct : indirect));
}

static int tile_in_quarter(int first, int oposite, int adjacent)
{
	double alfa = atan2(1, 3);
	double angle = atan2(fabs(oposite), fabs(adjacent));

	if (angle <= alfa)
		return (first);
	else if (angle < (M_PI/2) - alfa)
		return (first + 1);
	return (((first + 2 == 9) ? 1 : first + 2));
}

static int size_map(tile_t ***map, char c)
{
	int i = 0;
	if (c == 'y')
		for (i = 0; map[i]; i++);
	else if (c == 'x')
		for (i = 0; map[0][i]; i++);
	return (i);
}

static void broadcast_client(tile_t ***map, client_t *original, client_t *target, char *msg)
{
	int no_tile = 0;
	int x_path = 0;
	int y_path = 0;

	if (original->posX != target->posX || original->posY != target->posY) {
		x_path = smallest_path(original->posX, target->posX, size_map(map, 'x'));
		y_path = smallest_path(original->posY, target->posY, size_map(map, 'y'));
		if (x_path < 0 && y_path >= 0)
			no_tile = tile_in_quarter(1, y_path, x_path);
		else if (x_path >= 0 && y_path > 0)
			no_tile = tile_in_quarter(3, x_path, y_path);
		else if (x_path > 0 && y_path <= 0)
			no_tile = tile_in_quarter(5, y_path, x_path);
		else
			no_tile = tile_in_quarter(7, x_path, y_path);
	}
	dprintf(target->fd, "message %d, %s\n", no_tile, msg);
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

