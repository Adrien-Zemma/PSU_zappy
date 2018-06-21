/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	check_look_west(client_t *client, int *nb, int posX, server_t *server)
{
	int	posY = client->posY - 1;
	int	check;
	int	i = 0;

	do {
		posY++;
		if (posY - nb[0] < 0) {
			check = posY - nb[0];
			posY = server->parse->height - check;
			check_map(server->map[posY][posX], client);
		}
		else if (posY - nb[0] > (server->parse->height - 1)) {
			posY = posY - server->parse->height;
			check_map(server->map[posY - nb[0]][posX], client);
		}
		else{
			check_map(server->map[posY - nb[0]][posX], client);
		}
	}while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_west(server_t *server, client_t *client, int *nb)
{
	int	posX;

	dprintf(client->fd, "[");
	if (client->posX == 0)
		posX = server->parse->width - 1;
	else
		posX = client->posX - 1;
	for (int i = 0; i < client->level + 1; i++) {
		check_look_west(client, nb , posX, server);
		if (posX - 1 < 0)
			posX = server->parse->width - 1;
		else
			posX--;
		nb[0]++;
		nb[1]++;
	}
	return OK;
}
