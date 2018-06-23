/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	check_look_west(client_t *client,
			int *nb,
			int pos_x,
			server_t *server)
{
	int	pos_y = client->pos_y - 1;
	int	tmp;
	int	i = 0;

	do {
		pos_y = map_val_pos(server->parse->height, pos_y + 1);
		pos_x = map_val_pos(server->parse->width, pos_x);
		tmp = map_val_pos(server->parse->height, pos_y - nb[0]);
		check_map(server->map[tmp][pos_x], client);
	} while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_west(server_t *server, client_t *client, int *nb)
{
	int	pos_x;

	dprintf(client->fd, "[");
	pos_x = client->pos_x;
	for (int i = 0; i < client->level + 1; i++) {
		check_look_west(client, nb, pos_x, server);
		pos_x = map_val_pos(server->parse->width, pos_x - 1);
		nb[0]++;
		nb[1]++;
	}
	dprintf(client->fd, "]\n");
	return (OK);
}
