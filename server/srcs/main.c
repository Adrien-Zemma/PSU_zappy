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
	for (int i = 0; s->command[i]; i++)
		free(s->command[i]);
	free(s->command);
	for (int i = 0; s->clients[i];)
		remove_client(s, s->clients[i]->fd);
	free(s->teams);
	free(s->clients);
	for (int i = 0; s->parse->teams[i]; i++)
		free(s->parse->teams[i]);
	free(s->parse->teams);
	free(s->fds);
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

	signal(SIGINT, exit_handler);
	srand(time(NULL));
	if (!parse || ac < 12) {
		if (parse && parse->teams)
			free(parse->teams);
		free(parse);
		free(server);
		return (84);
	}
	if (set_struct_server(server, parse) == 84)
		return (84);
	free_tab(parse->teams);
	free(parse);
	return (0);
}
