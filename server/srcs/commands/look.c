/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** look
*/

#include "server.h"

void	check_map(tile_t *map, client_t *client)
{
	if (map->linemate != 0)
		dprintf(client->fd, "linemate ");
	if (map->deraumere != 0)
		dprintf(client->fd, "deraumere ");
	if (map->sibur != 0)
		dprintf(client->fd, "sibur ");
	if (map->mendiane != 0)
		dprintf(client->fd, "mendiane ");
	if (map->phiras != 0)
		dprintf(client->fd, "phiras ");
	if (map->thystam != 0)
		dprintf(client->fd, "thystam ");
	for (int i = 0; map->clients[i] != NULL; i++)
		dprintf(client->fd, "player ");
	if (map->food != 0)
		dprintf(client->fd, "food ");
	dprintf(client->fd, ",");
}

void	check_look_north(client_t *client, int *nb, int posY, server_t *server)
{
	int	posX = client->posX - 1;
	int	check;
	int	i = 0;

	do {
		posX++;
		if (posX - nb[0] < 0) {
			check = posX - nb[0];
			posX = server->parse->width - check;
			check_map(server->map[posY][posX], client);
		}
		else if (posX - nb[0] > (server->parse->width - 1)){
			posX = (posX) - server->parse->width;
			check_map(server->map[posY][posX - nb[0]], client);
		}
		else  {
			check_map(server->map[posY][posX - nb[0]], client);
		}
	} while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_north(server_t *server, client_t *client, int *nb)
{
	int	posY;

	dprintf(client->fd, "[");

	posY = client->posY;
	for (int i = 0; i < client->level + 1; i++) {
		check_look_north(client, nb, posY, server);
		if (posY - 1 < 0)
			posY = server->parse->height - 1;
		else
			posY--;
		nb[0]++;
		nb[1]++;
	}
	dprintf(client->fd, "]\n");
	return (0);
}

int	look(server_t *server, client_t *client, char *str)
{
	int	nb[2];

	nb[0] = 0;
	nb[1] = 0;
	str = str;
	switch (client->orientation){
		case 1:
			look_north(server, client, nb);
			break;
		case 3:
			look_south(server, client, nb);
			break;
		case 2:
			look_east(server, client, nb);
			break;
		case 4:
			look_west(server, client, nb);
			break;
	}

	return OK;
}
