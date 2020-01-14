--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: book; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.book (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    author character varying(50) NOT NULL,
    avg_rating double precision,
    format character varying(50),
    image character varying(100),
    num_pages integer,
    pub_date timestamp without time zone,
    pub_id integer
);


--
-- Name: book_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.book_id_seq OWNED BY public.book.id;


--
-- Name: publication; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.publication (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


--
-- Name: publication_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.publication_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: publication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.publication_id_seq OWNED BY public.publication.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    user_name character varying(20),
    user_email character varying(60),
    user_password character varying(60),
    registration_date timestamp without time zone
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: book id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.book ALTER COLUMN id SET DEFAULT nextval('public.book_id_seq'::regclass);


--
-- Name: publication id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication ALTER COLUMN id SET DEFAULT nextval('public.publication_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.book (id, title, author, avg_rating, format, image, num_pages, pub_date, pub_id) FROM stdin;
4	The Empty Book of Life	Roy Williamson	4.2	eBook	book-life-34063.svg	153	2019-12-01 14:42:03.259438	1
6	The Legend of Dracula	Charles Rowling	4.6	Hardcover	man-37603.svg	253	2019-12-01 14:42:03.259438	2
7	Taming Dragons	James Vonnegut	4.5	MassMarket Paperback	dragon-23164.svg	229	2019-12-01 14:42:03.259438	2
8	The Singing Magpie	Oscar Steinbeck	5	Hardcover	magpie-147852.svg	188	2019-12-01 14:42:03.259438	3
9	Mr. Incognito	Amelia Funke	4.2	Hardcover	incognito-160143.svg	205	2019-12-01 14:42:03.259438	3
10	A Dog without purpose	Edgar Dahl	4.8	MassMarket Paperback	dog-159271.svg	300	2019-12-01 14:42:03.259438	4
11	A Frog's Life	Herman Capote	3.9	MassMarket Paperback	amphibian-150342.svg	190	2019-12-01 14:42:03.259438	4
13	Thieves of Kaalapani	Mohit Gustav	4.1	Paperback	boat-1296201.svg	270	2019-12-01 14:42:03.259438	5
14	As Men Thinketh	Edward McPhee	4.5	Paperback	cranium-2028555.svg	124	2019-12-01 14:42:03.259438	6
15	Mathematics of Music	Mary Turing	4.5	Hardcover	music-306008.svg	120	2019-12-01 14:42:03.259438	6
16	The Mystery of Mandalas	Jack Morrison	4.2	Paperback	mandala-1817599.svg	221	2019-12-01 14:42:03.259438	6
17	The Sacred Book of Kairo	Heidi Zimmerman	3.8	ePub	book-1294676.svg	134	2019-12-01 14:42:03.259438	7
18	Love is forever, As Long as it lasts	Kovi O'Hara	4.5	Hardcover	love-2026554.svg	279	2019-12-01 14:42:03.259438	8
19	Order in Chaos	Wendy Sherman	3.5	MassMarket Paperback	chaos-1769656.svg	140	2019-12-01 14:42:03.259438	8
12	Logan Returns	Margaret Elliot	4.6	Hardcover	wolf-153648.svg	282	2019-12-01 14:42:03.259438	5
5	Life After Dealth	Nikita Kimmel	3.8	Hardback	mummy-146868.svg	175	2019-12-01 14:42:03.259438	2
20	Gulliver's Travels	Jonathan Swift	4.2	Paperback	gullivers-travels.jpg	543	2019-12-08 17:30:44.576934	1
21	Moby Dick	Herman Melville	5	Hardback	moby-dick.jpg	393	2019-12-08 17:30:44.576934	1
22	The Time Machine	H.G. Wells	4.1	Paperback	time-machine.png	297	2019-12-08 17:53:01.286889	3
23	Sherlock Holmes	Arthur Conan Doyle	4.9	Marketplace Paperback	sherlock-holmes.png	401	2019-12-08 17:53:01.286889	8
24	Robinson Crusoe	Daniel Defoe	4	Paperback	robinson-crusoe.jpg	452	2019-12-09 19:31:14.721234	5
\.


--
-- Data for Name: publication; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.publication (id, name) FROM stdin;
1	Oxford Publications
2	Paramount Press
3	Oracle Books Inc
4	Vintage Books and Comics
5	Trolls Press
6	Broadway Press
7	Downhill Publishers
8	Kingfisher Inc
9	Walton Press Inc.
10	Walton Press Inc.
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, user_name, user_email, user_password, registration_date) FROM stdin;
1	harry	harry@gmail.com	$2b$12$LITu00pr4UPFmoHXYPF7J.1briZIPcIHy0Zyi8bF5m5ai9Exs6Kfy	2019-12-02 18:21:12.553612
2	kev	kev@gmail.com	$2b$12$ZKCsDxEVId9iEqEL5JTP3.qTlBQcRJ2ypDUwMAM5MzCRmoP874izC	2019-12-05 20:47:18.849309
3	Tony	T@yahoo.ie	$2b$12$jvmWHfiQsBIi3OJNUWapFOBq4.Q8QoOWryDOhj8cN8hkzpUQ7GQfO	2019-12-05 20:49:46.255569
4	Test1	test@test.com	$2b$12$nb8nceDD4CKptqTLjX9KauPXp6wDTD1Hr2Mbbhd/42BCrWfwE1q6O	2019-12-08 13:44:46.437515
5	Test2	test2@test.com	$2b$12$y/Qa5Bze9QjsPk1v/GL11ukA37FzB6mBxVYmfd4DkCb8tEMFgTzvS	2019-12-09 19:31:45.104971
\.


--
-- Name: book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.book_id_seq', 24, true);


--
-- Name: publication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.publication_id_seq', 10, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- Name: book book_image_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_image_key UNIQUE (image);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (id);


--
-- Name: publication publication_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_book_title; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_book_title ON public.book USING btree (title);


--
-- Name: ix_users_user_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_users_user_email ON public.users USING btree (user_email);


--
-- Name: book book_pub_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pub_id_fkey FOREIGN KEY (pub_id) REFERENCES public.publication(id);


--
-- PostgreSQL database dump complete
--

