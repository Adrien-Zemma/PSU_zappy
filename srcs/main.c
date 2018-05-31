/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Main C file
*/

#include "server.h"

int main(int ac, char **av)
{
	t_parse	*parse = parse_args(av);
	server_t	*server = malloc(sizeof(server_t));
	
	server->fds = malloc(sizeof(int) * 1);
	server->nb_fd = 0;
	if (!parse || ac < 12) {
		if (parse && parse->teams)
			free(parse->teams);
		free(parse);
		return (84);
	}
	if (set_socket(parse, server) == 84)
		return (84);
	if (start_server(parse, server) == 84)
		return (84);
	free_tab(parse->teams);
	free(parse);
	return (0);
}