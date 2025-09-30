---
id: 52fbe7351e
question: Where does the number of Conv2d layer’s params come from? Where does the
  number of 'features' we get after the Flatten layer come from?
sort_order: 26
---

Let's say we define our Conv2d layer like this:

```python
 tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3))
```

This means our input image is RGB (3 channels, 150 by 150 pixels), the kernel is 3x3, and the number of filters (layer’s width) is 32.

If we check `model.summary()` we will get this:

```
_________________________________________________________________
Layer (type)                Output Shape              Param #
=================================================================
conv2d (Conv2D)             (None, 148, 148, 32)      896
```

So where do 896 params come from? It’s computed like this:

```python
(3*3*3 + 1) * 32
```

This results in 896:

- 3x3 kernel
- 3 channels RGB
- +1 for bias
- 32 filters


Number of 'Features' after the Flatten Layer

For our homework, `model.summary()` for the last MaxPooling2d and Flatten layers looked like this:

```
_________________________________________________________________
Layer (type)                Output Shape              Param #
=================================================================
max_pooling2d_3       (None, 7, 7, 128)         0
flatten (Flatten)           (None, 6272)              0
```

So where do 6272 vectors come from? It’s computed like this:

```python
7*7*128
```

This results in 6272:

- 7x7 "image shape" after several convolutions and poolings
- 128 filters

