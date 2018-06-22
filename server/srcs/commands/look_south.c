/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	check_look_south(client_t *client, int *nb, int pos_y, server_t *server)
{
	int	pos_x = client->pos_x - 1;
	int	tmp;
	int	i = 0;

	do {
		pos_y = map_val_pos(server->parse->height, pos_y);
		pos_x = map_val_pos(server->parse->width, pos_x + 1);
		tmp = map_val_pos(server->parse->width, pos_x + nb[0]);
		check_map(server->map[pos_y][tmp], client);
	} while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_south(server_t *server, client_t *client, int *nb)
{
	int	pos_y;

	dprintf(client->fd, "[");
	pos_y = client->pos_y;
	for (int i = 0; i < client->level + 1; i++) {
		check_look_south(client, nb, pos_y, server);
		pos_y = map_val_pos(server->parse->height, pos_y + 1);
		nb[0]++;
		nb[1]++;
	}
	dprintf(client->fd, "]\n");
	return (0);
}
