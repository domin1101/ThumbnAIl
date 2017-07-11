from model.Video import Video

class ThumbnailDataset:

    def __init__(self):
        self.videos = Video.select()
        self.next_index = 0

    def next_batch(self, batch_size):
        if self.next_index + batch_size < len(self.videos):
            batch = self.videos[self.next_index:self.next_index+batch_size]
            self.next_index += batch_size
        else:
            batch = self.videos[self.next_index:]
            self.next_index = 0
            batch += self.next_batch(batch_size - len(batch))

        return batch