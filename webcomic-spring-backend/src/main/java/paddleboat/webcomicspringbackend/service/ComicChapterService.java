package paddleboat.webcomicspringbackend.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.lang.Nullable;
import org.springframework.stereotype.Service;
import paddleboat.webcomicspringbackend.model.dto.ComicChapterDTO;
import paddleboat.webcomicspringbackend.model.entitiy.ComicChapter;
import paddleboat.webcomicspringbackend.service.cache.ComicCache;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class ComicChapterService {

    private final ComicCache comicCache;


    /**
     * Retrieves a ComicChapterDTO object based on the given chapterNumber.
     *
     * @param chapterNumber the chapter number
     * @return the ComicChapterDTO object if found, or null if not found
     */
    @Nullable
    public ComicChapterDTO getComicChapter(Integer chapterNumber) {
        ComicChapter chapter = this.comicCache.getComicChapter(chapterNumber);

        if (chapter == null) {
            log.warn("Got a null ComicPage from cache! [{}]", chapterNumber);
            return null;
        }

        return ComicChapterDTO.from(chapter, true, false);
    }

    public List<ComicChapterDTO> getAllComicChapters() {
        try {
            List<ComicChapter> chapters = this.comicCache.getAllChapters();
            List<ComicChapterDTO> response = new ArrayList<>();
            for (ComicChapter chapter : chapters) {
                response.add(ComicChapterDTO.from(chapter, false, true));
            }
            return response;
        } catch(RuntimeException e) {
            log.error("Problem getting all comic chapters!", e);
            throw e;
        }
    }
}
