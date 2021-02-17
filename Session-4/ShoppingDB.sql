CREATE TABLE customer(
	cust_id INT NOT NULL,
	f_name VARCHAR(20) NOT NULL,
	l_name VARCHAR(20) NOT NULL,
	PRIMARY KEY(cust_id)
);

CREATE TABLE order_tb(
	order_id INT NOT NULL,
	order_amt FLOAT NOT NULL,
	order_status VARCHAR(20) NOT NULL,
	customer_id INT NOT NULL,
	PRIMARY KEY(order_id),
	FOREIGN KEY (customer_id) REFERENCES customer(cust_id)
);

CREATE TABLE item(
	item_id INT NOT NULL,
	item_name VARCHAR(30) NOT NULL,
	item_cost FLOAT NOT NULL,
	PRIMARY KEY(item_id) 
);

CREATE TABLE orderitem(
	order_no INT NOT NULL,
	item_id INT NOT NULL,
	PRIMARY KEY(order_no, item_id)
);


INSERT INTO customer (cust_id,f_name,l_name) VALUES (001,'Nilesh','Sharma');
INSERT INTO customer (cust_id,f_name,l_name) VALUES (002,'Ramesh','Chaudhary');
INSERT INTO customer (cust_id,f_name,l_name) VALUES (003,'Rajat','Gaul');


INSERT INTO item (item_id, item_name, item_cost) VALUES (001, 'Shoes', 1500);
INSERT INTO item (item_id, item_name, item_cost) VALUES (002, 'Jacket', 750);
INSERT INTO item (item_id, item_name, item_cost) VALUES (003, 'Jeans', 1250);
INSERT INTO item (item_id, item_name, item_cost) VALUES (004, 'DSLR Camera', 12000);


INSERT INTO order_tb (order_id, order_amt, order_status, customer_id) VALUES (001, 2000, 'Delivered', 002);
INSERT INTO order_tb (order_id, order_amt, order_status, customer_id) VALUES (002, 750, 'Delivered', 001);
INSERT INTO order_tb (order_id, order_amt, order_status, customer_id) VALUES (003, 13500, 'In Process', 003);


INSERT INTO orderitem (order_no, item_id) VALUES (001, 002);
INSERT INTO orderitem (order_no, item_id) VALUES (001, 003);
INSERT INTO orderitem (order_no, item_id) VALUES (002, 002);
INSERT INTO orderitem (order_no, item_id) VALUES (003, 001);
INSERT INTO orderitem (order_no, item_id) VALUES (003, 004);


SELECT customer.cust_id, orderitem.order_no, orderitem.item_id
FROM ((order_tb 
INNER JOIN orderitem ON order_tb.order_id = orderitem.order_no)
INNER JOIN customer ON customer.cust_id = order_tb.customer_id);



