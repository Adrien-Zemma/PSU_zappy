/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	malloc_remove_client(server_t *server)
{
	server->clients[server->nb_client] = NULL;
	server->clients = realloc(server->clients,
		sizeof(client_t *) * (server->nb_client + 1));
	server->fds = realloc(server->fds,
		sizeof(int) * (server->nb_fd + 1));
}

void	remove_client(server_t *server, int fd)
{
	size_t	i = 0;
	size_t	j = 0;

	server->nb_client--;
	server->nb_fd--;
	for (; server->clients[i] && server->clients[j]; i++) {
		if (server->clients[j]->fd == fd) {
			if (server->clients[j]->id != -1
				&& server->clients[j]->team) {
				if (server->clients[j]->team->max_players
				> server->clients[j]->team->absolute_max_players)
					server->clients[j]->team->max_players--;
				server->clients[j]->team->current_players--;
			}
			free_queue(server->clients[j]->command);
			free(server->clients[j]);
			if (!server->clients[++j])
				break;
		}
		server->clients[i] = server->clients[j];
		server->fds[i] = server->fds[j++];
	}
	malloc_remove_client(server);
}

void	manage_error(int fd, int state, int *check)
{
	if (state != BAD_PARAM && state != KO)
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

void	check_read_command(server_t *server, char *str, int check)
{
	for (int j = 0; server->command[j]; j++) {
		if (strncmp(server->command[j]->name,
			str, strlen(server->command[j]->name)) == 0
		&& (strlen(str) == strlen(server->command[j]->name)
		|| str[strlen(server->command[j]->name)] == ' ')) {
			if (server->command[j]->time == 0)
				server->command[j]->ptrFnct(server,
					server->clients[check], str);
			else {
				queue_append(&server->clients[check]->command,
					copy_cmd(server->command[j], str));
				free(str);
			}
			return;
		}
	}
	free(str);
	dprintf(server->clients[check]->fd, "ko\n");
}

void	read_command(int c1, server_t *server)
{
	char	*str = getnextline(c1);
	int	check = 0;

	if (str == NULL) {
		remove_client(server, c1);
		return;
	}
	for (int i = 0; server->clients[i] != NULL; i++){
		if (server->clients[i]->fd == c1)
			check = i;
	}
	printf("Client[%d]: %s\n", c1, str);
	check_read_command(server, str, check);
}
