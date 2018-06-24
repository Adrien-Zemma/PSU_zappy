/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	map_size(server_t *server, client_t *client, char *str)
{
	(void)str;
	dprintf(client->fd,
		"msz %d %d\n",
		server->parse->width,
		server->parse->height);
	return (OK);
}

int	sgt(server_t *server, client_t *client, char *str)
{
	str = str;
	dprintf(client->fd, "sgt %d\n", server->parse->freq);
	return (OK);
}

int	sst(server_t *server, client_t *client, char *str)
{
	while (*str && *str != ' ')
		str++;
	if (*str == ' ')
		str++;
	else
		return (BAD_PARAM);
	server->parse->freq = atoi(str);
	dprintf(client->fd, "sst %d\n", server->parse->freq);
	return (OK);
}
