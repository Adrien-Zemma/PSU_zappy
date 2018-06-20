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
		dprintf(client->fd, "linemate");
	if (map->deraumere != 0)
		dprintf(client->fd, " deraumere");
	if (map->sibur != 0)
		dprintf(client->fd, " sibur");
	if (map->mendiane != 0)
		dprintf(client->fd, " mendiane");
	if (map->phiras != 0)
		dprintf(client->fd, " phiras");
	if (map->thystam != 0)
		dprintf(client->fd, " thystam");
	if (map->food != 0)
		dprintf(client->fd, " food,");
}

int	look_south(server_t *server, client_t *client, int j, int k)
{

	return (0);
}

int	look_north(server_t *server, client_t *client, int j, int k)
{
	int	posY;
	int	posX = client->posX;
	int	checkPosX = client->posX;
	int	check;

	dprintf(client->fd, "[");
	if (client->posY == 0)
		posY = server->parse->height - 1;
	else
		posY = client->posY - 1;
	for (int i = 0; i < client->level + 1; i++) {
		do {
			if (posX - j < 0) {
				check = posX - j;
				posX = server->parse->width - check;
				check_map(server->map[posY][posX], client);
			}
			else if (posX - j > server->parse->width - 1){
				posX = (posX - j) - server->parse->width - 1;
				check_map(server->map[posY][posX], client);
			}
			else
				check_map(server->map[posY][posX - j], client);

		} while (posX++ - j < checkPosX + k);
		j++;
		k++;
		if (posY - 1 == 0)
			posY = server->parse->height - 1;
		else
			posY--;
	}
	dprintf(client->fd, "]\n");
	return (0);
}

int	look(server_t *server, client_t *client, char *str)
{
	int	j = 0;
	int	k = 0;

	str = str;
	switch (client->orientation){
		case 1:
			look_north(server, client, j, k);
			break;
		case 2:
			look_south(server, client, j, k);
			break;
	}

	return OK;
}
