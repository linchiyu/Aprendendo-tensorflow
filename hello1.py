import tensorflow as tf

frase = tf.constant("oi")

with tf.Session() as sess:
	rodar = sess.run(frase)

print(rodar)