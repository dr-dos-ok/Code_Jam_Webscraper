 d e f   s o l v e ( l i n e ) : 
 	 l i n e   =   l i n e . s p l i t ( ) 
 	 
 	 m i n   =   i n t ( l i n e [ 0 ] ) 
 	 m a x   =   i n t ( l i n e [ 1 ] ) 
 	 
 	 n u m B e s t   =   0 
 	 
 	 f o r   n   i n   r a n g e ( m i n ,   m a x ) : 
 	 	 f o r   m   i n   r a n g e ( n + 1 ,   m a x + 1 ) : 
 	 	 	 i f   r e c y c l e d ( s t r ( n ) ,   s t r ( m ) ) : 
 	 	 	 	 n u m B e s t   + =   1 
 	 
 	 r e t u r n   n u m B e s t 
 
 
 d e f   r e c y c l e d ( n , m ) : 
 	 r e t u r n   l e n ( n )   = =   l e n ( m )   a n d   m   i n   n + n 
 
 	 
 
 w i t h   o p e n ( " i n p u t . t x t " ,   " r " )   a s   i n F i l e : 
 	 w i t h   o p e n ( " o u t p u t . t x t " ,   " w " )   a s   o u t F i l e : 
 	 	 i   =   - 1 
 	 	 f o r   l i n e   i n   i n F i l e : 
 	 	 	 i   + =   1 
 	 	 	 i f   i   = =   0 : 
 	 	 	 	 c o n t i n u e 
 	 	 	 
 	 	 	 n u m B e s t   =   s o l v e ( l i n e ) 
 	 	 	 
 	 	 	 t e x t   =   " C a s e   # % d :   % d "   %   ( i ,   n u m B e s t ) 
 	 	 	 o u t F i l e . w r i t e ( t e x t   +   " \ n " ) 
 
 
