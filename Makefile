NAME	= zappy_server

CC	= gcc

RM	= rm -f

SRCS	= ./server/srcs/commands.c \
	  ./server/srcs/main.c \
	  ./server/srcs/parse.c \
	  ./server/srcs/utils.c 

OBJS	= $(SRCS:.c=.o)

CFLAGS = -I ./server/incs/
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
