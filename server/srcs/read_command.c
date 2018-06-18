/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

static void	manage_error(int fd, int state, int *check)
{
	if (state != BAD_PARAM || state != KO)
		*check = 1;
	switch (state) {
		case BAD_PARAM:
		dprintf(fd, "sbp\n");
		break;
		case KO:
		dprintf(fd, "ko\n");
		break;
	}
}

void	read_command(int c1, server_t *server)
{
	char	*str = getnextline(c1);
	int	check = 0;
	int	state = 0;
	int	i = 0;

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
			server->clients[check]->command = server->command[j];
			// state = server->command[j]->ptrFnct(server, server->clients[check], str);
			// manage_error(c1, state, &i);
		}
	}
	if (!i)
		dprintf(c1, "suc:%d\n", i);
}
