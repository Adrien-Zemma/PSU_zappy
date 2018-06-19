/*
** EPITECH PROJECT, 2018
** zappy
** File description:
** timeout func
*/

#include "server.h"

struct timeval	*get_select_timeout(server_t *server)
{
	struct timeval	*ret = NULL;
	double		time_client = -1;
	size_t		i = 0;
	command_t	*cmd;

	for (i = 0; server->clients[i]; i++) {
		cmd = queue_get(&server->clients[i]->command);
		if (cmd && cmd->time > 0) {
			time_client = cmd->time;
			break;
		}
	}
	if (time_client == -1)
		return (NULL);
	for (; server->clients[i] != NULL; i++) {
		cmd = queue_get(&server->clients[i]->command);
		if (cmd && cmd->time > 0 && time_client > cmd->time)
			time_client = cmd->time;
	}
	ret = malloc(sizeof(struct timeval));
	if (!ret)
		return (NULL);
	ret->tv_sec = floor(time_client);
	ret->tv_usec = (double)(time_client - floor(time_client)) * 1000000.0f;
	return (ret);
}

void	remove_time_clients(server_t *server, double last_time)
{
	int		state;
	int		check = 0;
	command_t	*cmd = NULL;

	for (size_t i = 0; server->clients[i]; i++) {
		cmd = queue_get(&server->clients[i]->command);
		if (cmd) {
			cmd->time -= last_time;
			if (cmd->time - 0.001 < 0) {
				cmd = queue_pop(&server->clients[i]->command);
				state = cmd->ptrFnct(server,
					server->clients[i],
					cmd->name);
				free(cmd->name);
				free(cmd);
				cmd = NULL;
				manage_error(server->clients[i]->fd, state, &check);
				if (!check)
					dprintf(server->clients[i]->fd, "suc:%d\n", check);
			}
		}
	}
}

command_t	*copy_cmd(command_t *command, char *name)
{
	command_t	*ret = malloc(sizeof(command_t));

	if (!ret)
		return (NULL);
	ret->time = command->time;
	ret->ptrFnct = command->ptrFnct;
	ret->name = strdup(name);
	return (ret);
}
