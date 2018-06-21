/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Main C file
*/

#include "commands.h"
#include "parse.h"
#include "server.h"

static void exit_handler(int signal)
{
	(void)signal;
}

int	start_server(t_parse *parse, server_t *server)
{
	fd_set	readfds;

	while (42)
		if (check_fd(parse, server, readfds) == 84)
			return (84);
	return (0);
}

void	free_server(server_t *s)
{
	free(s->fds);
	for (int i = 0; s->command[i]; i++)
		free(s->command[i]);
	free(s->command);
	for (int i = 0; s->clients[i];)
		remove_client(s, s->clients[i]->fd);
	free(s->clients);
	for (int i = 0; s->parse->teams[i]; i++)
		free(s->parse->teams[i]);
	free(s->parse->teams);
	free_map(s->map);
	free(s->parse);
	free(s);
}

void	free_queue(command_t **queue)
{
	for (int i = 0; queue[i]; i++) {
		free(queue[i]->name);
		free(queue[i]);
	}
	free(queue);
}

int main(int ac, char **av)
{
	t_parse	*parse = parse_args(av);
	server_t	*server = malloc(sizeof(server_t));

	if (!parse || ac < 12) {
		if (parse && parse->teams)
			free(parse->teams);
		free(parse);
		free(server);
		return (84);
	}
	signal(SIGINT, exit_handler);
	server->clients = malloc(sizeof(client_t *) * 1);
	server->parse = parse;
	server->command = init_commands(parse);
	server->clients[0] = NULL;
	server->nb_client = 0;
	server->fds = malloc(sizeof(int) * 1);
	server->map = init_map(parse->width, parse->height);
	server->nb_fd = 0;
	if (set_socket(parse, server) == 84)
		return (84);
	if (start_server(parse, server) == 84)
		free_server(server);
		return (84);
	free_tab(parse->teams);
	free(parse);
	return (0);
}
