NAME	= server

CC	= gcc

RM	= rm -f

SRCS	= ./srcs/main.c \
	  ./srcs/parse.c \
	  ./srcs/utils.c \
	  ./srcs/set_socket.c \
	  ./srcs/server.c	\
	  ./srcs/getnextline.c

OBJS	= $(SRCS:.c=.o)

CFLAGS = -I ./incs/
CFLAGS += -W -Wall -Wextra -g3

all: $(NAME)

$(NAME): $(OBJS)
	 $(CC) $(OBJS) -o $(NAME) $(LDFLAGS)

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
