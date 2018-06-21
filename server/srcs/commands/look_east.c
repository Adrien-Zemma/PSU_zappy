/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	check_look_east(client_t *client, int *nb, int posX, server_t *server)
{
	int	posY = client->posY - 1;
	int	check;
	int	i = 0;

	do {
		posY++;
		if (posY - nb[0] < 0) {
			check = posY - nb[0];
			posY = server->parse->height - check;
			check_map(server->map[map_val_pos(server->parse->height, posY)][map_val_pos(server->parse->width, posX)], client);
		}
		else if (posY - nb[0] > (server->parse->height - 1)) {
			posY = posY - server->parse->height;
			check_map(server->map[map_val_pos(server->parse->height, posY - nb[0])][map_val_pos(server->parse->width, posX)], client);
		}
		else{
			check_map(server->map[map_val_pos(server->parse->height, posY - nb[0])][map_val_pos(server->parse->width, posX)], client);
		}
	}while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_east(server_t *server, client_t *client, int *nb)
{
	int	posX;

	dprintf(client->fd, "[");
	posX = client->posX;
	for (int i = 0; i < client->level + 1; i++) {
		check_look_east(client, nb, posX, server);
		if (posX + 1 > server->parse->width - 1)
			posX = 0;
		else
			posX++;
		nb[0]++;
		nb[1]++;
	}
	dprintf(client->fd, "]\n");
	return (0);
}
