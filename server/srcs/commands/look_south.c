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
	int	check;
	int	i = 0;

	do {
		pos_x++;
		if (pos_x - nb[0] < 0) {
			check = pos_x - nb[0];
			pos_x = server->parse->width - check;
			check_map(server->map[map_val_pos(server->parse->height, pos_y)][map_val_pos(server->parse->width, pos_x)], client);
		}
		else if (pos_x - nb[0] > (server->parse->width - 1)){
			pos_x = (pos_x) - server->parse->width;
			check_map(server->map[map_val_pos(server->parse->height, pos_y)][map_val_pos(server->parse->width, pos_x - nb[0])], client);
		}
		else
			check_map(server->map[map_val_pos(server->parse->height, pos_y)][map_val_pos(server->parse->width, pos_x - nb[0])], client);
	} while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_south(server_t *server, client_t *client, int *nb)
{
	int	pos_y;

	dprintf(client->fd, "[");
	pos_y = client->pos_y;
	for (int i = 0; i < client->level + 6; i++) {
		check_look_south(client, nb, pos_y, server);
		if (pos_y + 1 > server->parse->height - 1)
			pos_y = 0;
		else
			pos_y++;
		nb[0]++;
		nb[1]++;
	}
	dprintf(client->fd, "]\n");
	return (0);
}
