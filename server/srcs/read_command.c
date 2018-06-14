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
	printf("Client[%d]: %s\n", c1, str);
	fflush(NULL);
	for (int j = 0; server->command[j]; j++) {
		if (strncmp(server->command[j]->name, str, strlen(server->command[j]->name)) == 0) {
			server->command[j]->ptrFnct(server, server->clients[check], str);
			state = 1;
		}
	}
	if (!state && check != -1)
		dprintf(server->clients[check]->fd, "ko\n");
}