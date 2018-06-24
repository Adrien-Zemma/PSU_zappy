/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	check_str_accept(int tmp, char *str, server_t *server)
{
	if (!str)
		return (0);
	if (strcmp(str, "GRAPHIC") == 0) {
		free(str);
		return (set_graphic(server, tmp));
	}
	for (int i = 0; server->parse->teams[i] != NULL; i++)
		if (strncmp(server->parse->teams[i], str,
			strlen(server->parse->teams[i])) == 0)
			return (alloc_client(server, tmp, str));
	free(str);
	dprintf(tmp, "ko\n");
	return (0);
}

int	write_map(int tmp, client_t *client, server_t *server)
{
	dprintf(tmp, "%d\n",
		client->team->max_players - client->team->current_players);
	dprintf(tmp, "%d %d\n", server->parse->width, server->parse->height);
	send_connection(server->clients, client);
	return (tmp);
}
