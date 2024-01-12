package paddleboat.webcomicspringbackend.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import paddleboat.webcomicspringbackend.model.dto.ComicChapterDTO;
import paddleboat.webcomicspringbackend.model.dto.ComicPageDTO;
import paddleboat.webcomicspringbackend.model.system.AbstractBaseResource;
import paddleboat.webcomicspringbackend.model.PageIndex;
import paddleboat.webcomicspringbackend.service.ComicChapterService;
import paddleboat.webcomicspringbackend.service.ComicPageService;

import java.util.List;

@RestController
@RequestMapping("/comic")
@RequiredArgsConstructor
@Slf4j
public class ComicController extends AbstractBaseResource {

    private final ComicPageService comicPageService;
    private final ComicChapterService comicChapterService;

    @GetMapping("/{chapterNumber}/{pageNumber}/image")
    public ResponseEntity<byte[]> getComicPageImage(@PathVariable Integer chapterNumber, @PathVariable Integer pageNumber) throws Exception {
        try {
            PageIndex pageIndex = new PageIndex(chapterNumber, pageNumber);
            return success(comicPageService.getComicPageImage(pageIndex));
        } catch( Exception e) {
            log.error("Exception getting page image!", e);
            throw e;
        }
    }

    @GetMapping("/{chapterNumber}/{pageNumber}/info")
    public ResponseEntity<ComicPageDTO> getComicPage(@PathVariable Integer chapterNumber,
                                                     @PathVariable Integer pageNumber
    ) {
        try {
            PageIndex pageIndex = new PageIndex(chapterNumber, pageNumber);
            ComicPageDTO response = comicPageService.getComicPage(pageIndex);
            return success(response);
        } catch( RuntimeException e) {
            log.error("Exception getting page image!", e);
            throw e;
        }
    }

    @GetMapping("/{chapterNumber}/chapter")
    public ResponseEntity<ComicChapterDTO> getComicChapter(@PathVariable Integer chapterNumber) {
        try {
            return success(this.comicChapterService.getComicChapter(chapterNumber));
        } catch( RuntimeException e) {
            log.error("Exception getting chapter! [{}]", chapterNumber, e);
            throw e;
        }
    }

    @GetMapping("/all")
    public ResponseEntity<List<ComicChapterDTO>> getAllChapters() {
        return success(this.comicChapterService.getAllComicChapters());
    }
}
