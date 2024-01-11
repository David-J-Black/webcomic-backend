package paddleboat.webcomicspringbackend.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import paddleboat.webcomicspringbackend.model.PageIndex;
import paddleboat.webcomicspringbackend.model.entitiy.ComicPage;
import paddleboat.webcomicspringbackend.repository.ComicPageRepository;
import paddleboat.webcomicspringbackend.service.cache.ComicCache;

import java.nio.file.Files;
import java.nio.file.Paths;

@Service
@RequiredArgsConstructor
@Slf4j
public class ComicPageService {

    private final ComicCache comicCache;

    public byte[] getComicPageImage(PageIndex pageIndex) throws Exception {
        try {
            log.debug("Getting image for comic page [{}]", pageIndex);
            ComicPage page = comicCache.getPage(pageIndex);

            if (page == null) {
                log.error("Null page! [{}]", pageIndex);
                throw new Error("Null Page!");
            }

            if (page.getImageName() == null) {
                log.error("Page has no image name! [page: {}]", page);
            }

            return Files.readAllBytes(Paths.get("./pages/" + page.getImageName()));
        } catch (Exception e) {
            log.info(System.getProperty("user.dir"));
            log.error("Error retreiving comic image", e);
            throw e;
        }
    }

//    public List<ComicPageDTO> getComicPages {
//        this.comicCache
//    }
}
