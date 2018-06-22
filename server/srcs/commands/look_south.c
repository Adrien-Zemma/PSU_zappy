/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	check_look_south(client_t *client, int *nb, int posY, server_t *server)
{
	int	posX = client->posX - 1;
	int	check;
	int	i = 0;

	do {
		posX++;
		if (posX - nb[0] < 0) {
			check = posX - nb[0];
			posX = server->parse->width - check;
			check_map(server->map[map_val_pos(server->parse->height, posY)][map_val_pos(server->parse->width, posX)], client);
		}
		else if (posX - nb[0] > (server->parse->width - 1)){
			posX = (posX) - server->parse->width;
			check_map(server->map[map_val_pos(server->parse->height, posY)][map_val_pos(server->parse->width, posX - nb[0])], client);
		}
		else
			check_map(server->map[map_val_pos(server->parse->height, posY)][map_val_pos(server->parse->width, posX - nb[0])], client);
	} while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_south(server_t *server, client_t *client, int *nb)
{
	int	posY;

	dprintf(client->fd, "[");
	posY = client->posY;
	for (int i = 0; i < client->level + 6; i++) {
		check_look_south(client, nb, posY, server);
		if (posY + 1 > server->parse->height - 1)
			posY = 0;
		else
			posY++;
		nb[0]++;
		nb[1]++;
	}
	dprintf(client->fd, "]\n");
	return (0);
}
