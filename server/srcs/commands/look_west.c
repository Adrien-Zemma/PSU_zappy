/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	check_look_west(client_t *client, int *nb, int pos_x, server_t *server)
{
	int	pos_y = client->pos_y - 1;
	int	check;
	int	i = 0;

	do {
		pos_y++;
		if (pos_y - nb[0] < 0) {
			check = pos_y - nb[0];
			pos_y = server->parse->height - check;
			check_map(server->map[map_val_pos(server->parse->height, pos_y)][map_val_pos(server->parse->width, pos_x)], client);
		}
		else if (pos_y - nb[0] > (server->parse->height - 1)) {
			pos_y = pos_y - server->parse->height;
			check_map(server->map[map_val_pos(server->parse->height, pos_y - nb[0])][map_val_pos(server->parse->width, pos_x)], client);
		}
		else{
			check_map(server->map[map_val_pos(server->parse->height, pos_y - nb[0])][map_val_pos(server->parse->width, pos_x)], client);
		}
	}while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_west(server_t *server, client_t *client, int *nb)
{
	int	pos_x;

	dprintf(client->fd, "[");
	pos_x = client->pos_x;
	for (int i = 0; i < client->level + 1; i++) {
		check_look_west(client, nb, pos_x, server);
		if (pos_x - 1 < 0)
			pos_x = server->parse->width - 1;
		else
			pos_x--;
		nb[0]++;
		nb[1]++;
	}
	dprintf(client->fd, "]");
	return OK;
}
