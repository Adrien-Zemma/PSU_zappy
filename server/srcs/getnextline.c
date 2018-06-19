/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** getnextline
*/

#include "server.h"

char	*gnl_realloc(char *str, int size)
{
	char	*ret;
	int	i;

	size += strlen(str);
	ret = malloc(sizeof(char) * (size + 1));
	if (ret == NULL)
		return (NULL);
	memset(ret, 0, size + 1);
	i = 0;
	while (str[i] != 0) {
		ret[i] = str[i];
		i++;
	}
	free(str);
	return (ret);
}

char	*gnl_ret(char *ret)
{
	int	len = strlen(ret);

	if (len == 0) {
		free(ret);
		return (NULL);
	}
	if (ret[len - 1] == '\n' || ret[len - 1] == '\r')
		ret[len - 1] = 0;
	return (ret);
}

char	*getnextline(int fd)
{
	char	*ret = malloc(sizeof(char) * 2);
	char	c;
	int	i;

	if (ret == NULL)
		return (NULL);
	memset(ret, 0, 2);
	i = 0;
	c = 1;
	while (c != 0 && c != '\n' && c != '\r') {
		if (read(fd, &c, 1) < 1)
			return (gnl_ret(ret));
		ret[i] = c;
		ret = gnl_realloc(ret, i + 1);
		if (ret == NULL)
			return (NULL);
		i++;
	}
	return (gnl_ret(ret));
}
