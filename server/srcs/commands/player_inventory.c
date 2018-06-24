/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

static void	print_player_inventory(client_t *client, int fd, int id)
{
	dprintf(fd, "pin %d %d %d %d %d %d %d %d %d %d\n",
		id, client->pos_x, client->pos_y,
		client->food, client->linemate,
		client->demaumere, client->sibur,
		client->mendiane, client->phiras,
		client->thystame);
}

int	player_inventory(server_t *server, client_t *client, char *str)
{
	int	id;

	while (*str && *str != '#')
		str++;
	if (*str == '#')
		str++;
	else
		return (BAD_PARAM);
	id = atoi(str);
	for (int i = 0; server->clients[i] != NULL; i++) {
		if (server->clients[i]->id == id)
			print_player_inventory(server->clients[i],
						client->fd, id);
	}
	return (OK);
}
