/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** look
*/

#include "server.h"

int	map_val_pos(int map_size, int pos)
{
	while (pos < 0)
		pos += map_size;
	while (pos >= map_size)
		pos -= map_size;
	return pos;
}

void	check_look_north(client_t *client,
	int *nb, int pos_y, server_t *server)
{
	int	pos_x = client->pos_x - 1;
	int	check;
	int	i = 0;

	do {
		pos_x++;
		if (pos_x - nb[0] < 0) {
			check = pos_x - nb[0];
			pos_x = server->parse->width - check;
			check_map(server->map[map_val_pos(server->parse->height,
				pos_y)][map_val_pos(server->parse->width, pos_x)],
				client);
		}
		else if (pos_x - nb[0] > (server->parse->width - 1)){
			pos_x = (pos_x) - server->parse->width;
			check_map(server->map[map_val_pos(server->parse->height,
				pos_y)][map_val_pos(server->parse->width,
				pos_x - nb[0])], client);
		}
		else  {
			check_map(server->map[map_val_pos(server->parse->height,
				pos_y)][map_val_pos(server->parse->width,
				pos_x - nb[0])], client);
		}
	} while (i++ - nb[0] < 1 + nb[0] - 1);
}

int	look_north(server_t *server, client_t *client, int *nb)
{
	int	pos_y;

	dprintf(client->fd, "[");

	pos_y = client->pos_y;
	for (int i = 0; i < client->level + 1; i++) {
		check_look_north(client, nb, pos_y, server);
		if (pos_y - 1 < 0)
			pos_y = server->parse->height - 1;
		else
			pos_y--;
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
	return (OK);
}
