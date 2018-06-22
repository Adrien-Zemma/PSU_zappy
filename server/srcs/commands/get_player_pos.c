/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	get_player_pos(server_t *server, client_t *client, char *str)
{
	int client_id = -1;
	client_t	*c;

	while (*str && *str != ' ')
		str++;
	if (*str == ' ' && *(str + 1) && *(str + 1) == '#')
		str++;
	else
		return (BAD_PARAM);
	str++;
	client_id = atoi(str);
	printf("hello:%d|%s\n", client_id, str);
	fflush(NULL);
	for (int i = 0; server->clients[i]; i++) {
		printf("Client:%d|%d\n", client_id, server->clients[i]->id);
		if (server->clients[i]->id == client_id) {
			c = server->clients[i];
			dprintf(client->fd, "ppo %d %d %d %d\n",
			client_id, c->pos_x, c->pos_y,
			c->orientation);
		}
	}
	return (OK);
}
