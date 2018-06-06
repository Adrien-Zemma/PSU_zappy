/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	read_command(int c1, server_t *server)
{
	char	*str = getnextline(c1);
	int	check = -1;
	int	state = 0;
	
	if (str == NULL)
		return ;
	for (int i = 0; server->clients[i] != NULL; i++){
		if (server->clients[i]->fd == c1)
			check = i;
	}
	for (int j = 0; server->command[j]; j++) {
		if (strncmp(server->command[j]->name, str, strlen(server->command[j]->name)) == 0) {
			server->command[j]->ptrFnct(server, server->clients[check], str);
			state = 1;
		}
	}
	if (!state && check != -1)
		dprintf(server->clients[check]->fd, "ko\n");
}

void	map_size(server_t *server, client_t *client, char *str)
{
	str = str;
	dprintf(client->fd, "msz %d %d\n", server->parse->width, server->parse->height);
}

void	all_team(server_t *server, client_t *client, char *str)
{
	str = str;
	for (int i = 0; server->parse->teams[i] != NULL; i++)
		dprintf(client->fd, "tna %s\n", server->parse->teams[i]);
}