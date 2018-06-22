/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	set_port(t_parse *parse, server_t *server)
{
	struct	sockaddr_in	s_in;

	s_in.sin_family = AF_INET;
	s_in.sin_port = htons(parse->port);
	printf("port: %d\n", parse->port);
	s_in.sin_addr.s_addr = INADDR_ANY;
	if (bind(server->fd, (const struct sockaddr *)&s_in,
		sizeof(s_in)) == -1){
		close (server->fd);
		return (84);
	}
	if (listen(server->fd, SOMAXCONN) == -1){
		close(server->fd);
		return (84);
	}
	return (0);
}

int	set_socket(t_parse *parse, server_t *server)
{
	struct	protoent	*pe;
	pe = getprotobyname("TCP");
	if (!pe)
		return (84);
	server->fd = socket(AF_INET, SOCK_STREAM, pe->p_proto);
	if (server->fd == -1)
		return (84);
	return (set_port(parse, server));
}
